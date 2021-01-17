package org.ztech.drakonide.impl;

import com.intellij.openapi.components.PersistentStateComponent;
import com.intellij.openapi.module.Module;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;
import org.ztech.drakonide.IDrakonService;

/**
 * @see IDrakonService
 */
public class DrakonServiceImpl implements IDrakonService, PersistentStateComponent {
    public DrakonServiceImpl(Module project) {
    }

    @Nullable
    @Override
    public Object getState() {
        return null;
    }

    @Override
    public void loadState(@NotNull Object o) {

    }
}
