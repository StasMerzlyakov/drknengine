package org.ztech.drakonide;

import com.intellij.openapi.module.Module;
import org.jetbrains.annotations.NotNull;

/**
 * Интерфейс копмонана уровня модуля, добавлюящий функционал для разработки DRAKON-схем
 */
public interface IDrakonService {
    static IDrakonService getInstance(@NotNull Module module) {
        return module.getService(IDrakonService.class);
    }
}
